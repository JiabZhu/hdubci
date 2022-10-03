export interface offExperienceInt {
    target_proportion: number | undefined,
    non_target_proportion: number | undefined,
    trial_num: number | undefined,
    target_mark: number | undefined,
    non_target_mark: number | undefined,
    fixation_duration: number | undefined,
    pic_duration: number | undefined,
    fixation_pic: string | undefined,
    target_pic_list: string[],
    non_target_pic_list: string[],
    end_pic: string | undefined,
}
export class OffExperience {
    experienceData: offExperienceInt = {
        target_proportion: undefined,
        non_target_proportion: undefined,
        trial_num: undefined,
        target_mark: undefined,
        non_target_mark: undefined,
        fixation_duration: undefined,
        pic_duration: undefined,
        fixation_pic: "",
        target_pic_list: [],
        non_target_pic_list: [],
        end_pic: "",
    }
}